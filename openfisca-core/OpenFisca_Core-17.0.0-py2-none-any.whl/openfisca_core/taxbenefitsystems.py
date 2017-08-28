# -*- coding: utf-8 -*-


import glob
from inspect import isclass
from os import path, linesep
from imp import find_module, load_module
import importlib
import logging
import inspect
import pkg_resources
import warnings
import traceback

from setuptools import find_packages

import conv
from parameters import ParameterNode
from variables import Variable
from scenarios import AbstractScenario
from formulas import get_neutralized_column

log = logging.getLogger(__name__)


class VariableNotFound(Exception):
    """Exception raised when a variable has been queried but is not defined in the TaxBenefitSystem.
    """

    def __init__(self, variable_name, tax_benefit_system):
        """
        :param variable_name: Name of the variable that was queried.
        :param tax_benefit_system: Tax benefits system that does not contain `variable_name`
        """
        country_package_metadata = tax_benefit_system.get_package_metadata()
        country_package_name = country_package_metadata['name']
        country_package_version = country_package_metadata['version']
        if country_package_version:
            country_package_id = '{}@{}'.format(country_package_name, country_package_version)
        else:
            country_package_id = country_package_name
        message = linesep.join([
            u"You tried to calculate or to set a value for variable '{0}', but it was not found in the loaded tax and benefit system ({1}).".format(variable_name, country_package_id),
            u"Are you sure you spelled '{0}' correctly?".format(variable_name),
            u"If this code used to work and suddenly does not, this is most probably linked to an update of the tax and benefit system.",
            u"Look at its changelog to learn about renames and removals and update your code. If it is an official package,",
            u"it is probably available on <https://github.com/openfisca/{0}/blob/master/CHANGELOG.md>.".format(country_package_name)
            ])
        Exception.__init__(self, message.encode('utf-8'))


class VariableNameConflict(Exception):
    """
    Exception raised when two variables with the same name are added to a tax and benefit system.
    """
    pass


class TaxBenefitSystem(object):
    """
    Represents the legislation.

    It stores parameters (values defined for everyone) and variables (values defined for some given entity e.g. a person).

    :param entities: Entities used by the tax benefit system.
    :param string parameters: Directory containing the YAML parameter files.


    .. py:attribute:: parameters

       :any:`ParameterNode` containing the legislation parameters
    """
    _base_tax_benefit_system = None
    _parameters_at_instant_cache = None
    person_key_plural = None
    preprocess_parameters = None
    json_to_attributes = staticmethod(conv.pipe(
        conv.test_isinstance(dict),
        conv.struct({}),
        ))
    baseline = None  # Baseline tax-benefit system. Used only by reforms. Note: Reforms can be chained.
    Scenario = AbstractScenario
    cache_blacklist = None
    decomposition_file_path = None

    def __init__(self, entities):
        # TODO: Currently: Don't use a weakref, because they are cleared by Paste (at least) at each call.
        self._parameters_at_instant_cache = {}  # weakref.WeakValueDictionary()
        self.column_by_name = {}
        self.automatically_loaded_variable = set()

        self.entities = entities
        if entities is None or len(entities) == 0:
            raise Exception("A tax and benefit sytem must have at least an entity.")
        self.person_entity = [entity for entity in entities if entity.is_person][0]
        self.group_entities = [entity for entity in entities if not entity.is_person]

    @property
    def base_tax_benefit_system(self):
        base_tax_benefit_system = self._base_tax_benefit_system
        if base_tax_benefit_system is None:
            baseline = self.baseline
            if baseline is None:
                return self
            self._base_tax_benefit_system = base_tax_benefit_system = baseline.base_tax_benefit_system
        return base_tax_benefit_system

    @classmethod
    def json_to_instance(cls, value, state = None):
        attributes, error = conv.pipe(
            cls.json_to_attributes,
            conv.default({}),
            )(value, state = state or conv.default_state)
        if error is not None:
            return attributes, error
        return cls(**attributes), None

    def new_scenario(self):
        scenario = self.Scenario()
        scenario.tax_benefit_system = self
        return scenario

    def prefill_cache(self):
        pass

    def load_variable(self, variable_class, update = False):
        name = unicode(variable_class.__name__)
        variable_type = variable_class.__bases__[0]
        attributes = dict(variable_class.__dict__)

        # Check if a Variable of same name is already registered.
        existing_column = self.get_column(name)
        if existing_column:
            if update:
                attributes['baseline_variable'] = existing_column
            else:
                # Variables that are dependencies of others (trough a conversion column) can be loaded automatically
                # Is it still necessary ?
                if name in self.automatically_loaded_variable:
                    self.automatically_loaded_variable.remove(name)
                    return self.get_column(name)
                raise VariableNameConflict(
                    u'Variable "{}" is already defined. Use `update_variable` to replace it.'.format(name))

        # We pass the variable_class just for introspection.
        variable = variable_type(name, attributes, variable_class)
        # We need the tax and benefit system to identify columns mentioned by conversion variables.
        column = variable.to_column(self)
        self.add_column(column)

        return column

    def add_variable(self, variable):
        """
        Adds an OpenFisca variable to the tax and benefit system.

        :param variable: The variable to add. Must be a subclass of Variable.

        :raises: :any:`VariableNameConflict` if a variable with the same name have previously been added to the tax and benefit system.
        """
        return self.load_variable(variable, update = False)

    def update_variable(self, variable):
        """
        Replaces an existing OpenFisca variable in the tax and benefit system by a new one.

        The new variable must have the same name than the old one.

        If no variable with the given name exists in the tax and benefit system, no error will be raised and the variable will be simply added.

        :param variable: Variable to add. Must be a subclass of Variable.
        """
        return self.load_variable(variable, update = True)

    def add_variables_from_file(self, file_path):
        """
        Adds all OpenFisca variables contained in a given file to the tax and benefit system.
        """
        try:
            module_name = path.splitext(path.basename(file_path))[0]
            module_directory = path.dirname(file_path)
            try:
                module = load_module(module_name, *find_module(module_name, [module_directory]))
            except NameError as e:
                logging.error(str(e) + ": if this code used to work, this error might be due to a major change in OpenFisca-Core. Checkout the changelog to learn more: <https://github.com/openfisca/openfisca-core/blob/master/CHANGELOG.md>")
                raise
            potential_variables = [getattr(module, item) for item in dir(module) if not item.startswith('__')]
            for pot_variable in potential_variables:
                # We only want to get the module classes defined in this module (not imported)
                if isclass(pot_variable) and \
                        issubclass(pot_variable, Variable) and \
                        pot_variable.__module__.endswith(module_name):
                    self.add_variable(pot_variable)
        except:
            log.error(u'Unable to load OpenFisca variables from file "{}"'.format(file_path))
            raise

    def add_variables_from_directory(self, directory):
        """
        Recursively explores a directory, and adds all OpenFisca variables found there to the tax and benefit system.
        """
        py_files = glob.glob(path.join(directory, "*.py"))
        for py_file in py_files:
            self.add_variables_from_file(py_file)
        subdirectories = glob.glob(path.join(directory, "*/"))
        for subdirectory in subdirectories:
            self.add_variables_from_directory(subdirectory)

    def add_variables(self, *variables):
        """
        Adds a list of OpenFisca Variables to the `TaxBenefitSystem`.

        See also :any:`add_variable`
        """
        for variable in variables:
            self.add_variable(variable)

    def load_extension(self, extension):
        """
        Loads an extension to the tax and benefit system.

        :param string extension: The extension to load. Can be an absolute path pointing to an extension directory, or the name of an OpenFisca extension installed as a pip package.

        """
        if path.isdir(extension):
            if find_packages(extension):
                # Load extension from a package directory
                extension_directory = path.join(extension, find_packages(extension)[0])
            else:
                # Load extension from a simple directory
                extension_directory = extension
        else:
            # Load extension from installed pip package
            try:
                package = importlib.import_module(extension)
                extension_directory = package.__path__[0]
            except ImportError:
                message = linesep.join([traceback.format_exc(),
                                        u'Error loading extension: `{}` is neither a directory, nor a package.'.format(extension),
                                        u'Are you sure it is installed in your environment? If so, look at the stack trace above to determine the origin of this error.',
                                        u'See more at <https://github.com/openfisca/openfisca-extension-template#installing>.'])
                raise ValueError(message)

        self.add_variables_from_directory(extension_directory)
        param_dir = path.join(extension_directory, 'parameters')
        if path.isdir(param_dir):
            extension_parameters = ParameterNode(directory_path = param_dir)
            self.parameters.merge(extension_parameters)

    def apply_reform(self, reform_path):
        """
        Generates a new tax and benefit system applying a reform to the tax and benefit system.

        The current tax and benefit system is **not** mutated.

        :param string reform_path: The reform to apply. Must respect the format *installed_package.sub_module.reform*

        :returns: A reformed tax and benefit system.

        Exemple:

        >>> self.apply_reform('openfisca_france.reforms.inversion_revenus')

        """
        from reforms import Reform
        try:
            reform_package, reform_name = reform_path.rsplit('.', 1)
        except ValueError:
            raise ValueError(u'`{}` does not seem to be a path pointing to a reform. A path looks like `some_country_package.reforms.some_reform.`'.format(reform_path).encode('utf-8'))
        try:
            reform_module = importlib.import_module(reform_package)
        except ImportError:
            message = linesep.join([traceback.format_exc(),
                                    u'Could not import `{}`.'.format(reform_package).encode('utf-8'),
                                    u'Are you sure of this reform module name? If so, look at the stack trace above to determine the origin of this error.'])
            raise ValueError(message)
        reform = getattr(reform_module, reform_name, None)
        if reform is None:
            raise ValueError(u'{} has no attribute {}'.format(reform_package, reform_name).encode('utf-8'))
        if not issubclass(reform, Reform):
            raise ValueError(u'`{}` does not seem to be a valid Openfisca reform.'.format(reform_path).encode('utf-8'))

        return reform(self)

    def add_column(self, column):
        self.column_by_name[column.name] = column

    def get_column(self, column_name, check_existence = False):
        column = self.column_by_name.get(column_name)
        if not column and check_existence:
            raise VariableNotFound(column_name, self)
        return column

    def update_column(self, column_name, new_column):
        self.column_by_name[column_name] = new_column

    def neutralize_variable(self, variable_name):
        """
        Neutralizes an OpenFisca variable existing in the tax and benefit system.

        A neutralized variable always returns its default value when computed.

        Trying to set inputs for a neutralized variable has no effect except raising a warning.
        """
        self.update_column(variable_name, get_neutralized_column(self.get_column(variable_name)))

    def neutralize_column(self, column_name):
        warnings.warn(
            u"The neutralize_column method has been renamed to neutralize_variable. "
            u"neutralize_column has thus been deprecated and will be removed in the next major version. "
            u"Please update your code.",
            Warning
            )
        self.neutralize_variable(column_name)

    def load_parameters(self, path_to_yaml_dir):
        """
        Loads the legislation parameter for a directory containing YAML parameters files.

        :param path_to_yaml_dir: Absolute path towards the YAML parameter directory.

        Exemples:

        >>> self.load_parameters('/path/to/yaml/parameters/dir')
        """

        parameters = ParameterNode('', directory_path = path_to_yaml_dir)

        if self.preprocess_parameters is not None:
            parameters = self.preprocess_parameters(parameters)

        self.parameters = parameters

    def _get_baseline_parameters_at_instant(self, instant):
        baseline = self.baseline
        if baseline is None:
            return self.get_parameters_at_instant(instant)
        return baseline._get_baseline_parameters_at_instant(instant)

    def get_parameters_at_instant(self, instant):
        """Compute the parameters of the legislation at a given instant

        :param instant: string of the format 'YYYY-MM-DD' or `openfisca_core.periods.Instant` instance.
        :returns: The parameters of the legislation at a given instant.
        """

        parameters = self.parameters
        instant_str = str(instant)
        parameters_at_instant = self._parameters_at_instant_cache.get(instant)
        if parameters_at_instant is None and parameters is not None:
            parameters_at_instant = parameters._get_at_instant(instant_str)
            self._parameters_at_instant_cache[instant] = parameters_at_instant
        return parameters_at_instant

    def get_package_metadata(self):
        """
            Gets metatada relative to the country package the tax and benefit system is built from.

            :returns: Country package metadata
            :rtype: dict

            Exemple:

            >>> tax_benefit_system.get_package_metadata()
            >>> {
            >>>    'location': '/path/to/dir/containing/package',
            >>>    'name': 'openfisca-france',
            >>>    'repository_url': 'https://github.com/openfisca/openfisca-france',
            >>>    'version': '17.2.0'
            >>>    }
        """
        # Handle reforms
        if self.baseline:
            return self.baseline.get_package_metadata()

        fallback_metadata = {
            'name': self.__class__.__name__,
            'version': '',
            'repository_url': '',
            'location': '',
            }

        module = inspect.getmodule(self)
        if not module.__package__:
            return fallback_metadata
        package_name = module.__package__.split('.')[0]
        try:
            distribution = pkg_resources.get_distribution(package_name)
        except pkg_resources.DistributionNotFound:
            return fallback_metadata

        location = inspect.getsourcefile(module).split(package_name)[0].rstrip('/')

        home_page_metadatas = [
            metadata.split(':', 1)[1].strip(' ')
            for metadata in distribution._get_metadata(distribution.PKG_INFO) if 'Home-page' in metadata
            ]
        repository_url = home_page_metadatas[0] if home_page_metadatas else ''
        return {
            'name': distribution.key,
            'version': distribution.version,
            'repository_url': repository_url,
            'location': location,
            }

    def get_variables(self, entity = None):
        """
        Gets all variables contained in a tax and benefit system.

        :param <Entity subclass> entity: If set, returns only the variable defined for the given entity.

        :returns: A dictionnary, indexed by variable names.
        :rtype: dict

        """
        if not entity:
            return self.column_by_name
        else:
            return {
                variable_name: variable
                for variable_name, variable in self.column_by_name.iteritems()
                if variable.entity == entity
                }
