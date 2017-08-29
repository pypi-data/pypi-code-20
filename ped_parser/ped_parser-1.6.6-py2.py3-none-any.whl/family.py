#!/usr/bin/env python
# encoding: utf-8
"""
family.py

Holds the meta information of a family and its individuals.

    - has a Individual

Attributes:

individuals DICT dictionary with family members on the form {<ind_id>:<Individual_obj>}
variants DICT dictionary with all the variants that exists in the family on the form {<var_id>:<Variant_obj>}


Created by Måns Magnusson on 2014-02-05.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import logging

from ped_parser.exceptions import PedigreeError


class Family(object):
    """Base class for the family parsers."""
    def __init__(self, family_id, individuals = {}, models_of_inheritance=set([]),
                logger=None, logfile=None, loglevel=None):
        super(Family, self).__init__()
        self.logger = logging.getLogger(__name__)
        
        # Each family needs to have a family id
        self.family_id = family_id
        self.logger.debug("Initiating family with id:{0}".format(self.family_id))
        
         # This is a dict with individual objects
        self.individuals = individuals
        self.logger.debug("Adding individuals:{0}".format(
            ','.join([ind for ind in self.individuals])
        ))
        
        # List of models of inheritance that should be prioritized.
        self.models_of_inheritance = models_of_inheritance 
        self.logger.debug("Adding models of inheritance:{0}".format(
            ','.join(self.models_of_inheritance)
            )
        )
        
        #Trios are a list of sets with trios.
        self.trios = []
        #Duos are a list of sets with trios.
        self.duos = []
        # Bool if there are any relations in the family
        self.no_relations = True
        # Set of affected individual id:s
        self.affected_individuals = set()
    
    def family_check(self):
        """
        Check if the family members break the structure of the family. 
        
        eg. nonexistent parent, wrong sex on parent etc. 
        
        Also extracts all trios found, this is of help for many at the moment 
        since GATK can only do phasing of trios and duos.
        """
        #TODO Make some tests for these
        self.logger.debug("Checking family relations for {0}".format(
            self.family_id)
        )
        for individual_id in self.individuals:
            
            self.logger.debug("Checking individual {0}".format(individual_id))
            individual = self.individuals[individual_id]
            
            self.logger.debug("Checking if individual {0} is affected".format(
                individual_id))
            
            if individual.affected:
                self.logger.debug("Found affected individual {0}".format(
                    individual_id)
                )
                self.affected_individuals.add(individual_id)
            
            father = individual.father
            mother = individual.mother
            
            if individual.has_parents:
                self.logger.debug("Individual {0} has parents".format(
                    individual_id))
                self.no_relations = False
                try:
                    self.check_parent(father, father=True)
                    self.check_parent(mother, father=False)
                except PedigreeError as e:
                    raise e
                
                # Check if there is a trio
                if individual.has_both_parents:
                    self.trios.append(set([individual_id, father, mother]))
                elif father != '0':
                    self.duos.append(set([individual_id, father]))
                else:
                    self.duos.append(set([individual_id, mother]))
                
                ##TODO self.check_grandparents(individual)
            
            # Annotate siblings:
            for individual_2_id in self.individuals:
                if individual_id != individual_2_id:
                    if self.check_siblings(individual_id, individual_2_id):
                        individual.siblings.add(individual_2_id)
                    ##TODO elif self.check_cousins(individual_id, individual_2_id):
                    #     individual.cousins.add(individual_2_id)
    
    def check_parent(self, parent_id, father = False):
        """
        Check if the parent info is correct. If an individual is not present in file raise exeption.

        Input: An id that represents a parent
               father = True/False

        Raises SyntaxError if
            The parent id is not present
            The gender of the parent is wrong.
        """
        self.logger.debug("Checking parent {0}".format(parent_id))
        if parent_id != '0':
            if parent_id not in self.individuals:
                raise PedigreeError(self.family_id, parent_id, 
                                    'Parent is not in family.')
            if father:
                if self.individuals[parent_id].sex != 1:
                    raise PedigreeError(self.family_id, parent_id, 
                                        'Father is not specified as male.')
            else:
                if self.individuals[parent_id].sex != 2:
                    raise PedigreeError(self.family_id, parent_id, 
                                        'Mother is not specified as female.')
        return
    
    def check_siblings(self, individual_1_id, individual_2_id):
        """
        Check if two family members are siblings.
        
        Arguments: 
            individual_1_id (str): The id of an individual
            individual_2_id (str): The id of an individual
        
        Returns: 
            bool : True if the individuals are siblings
                   False if they are not siblings
        """
        
        self.logger.debug("Checking if {0} and {1} are siblings".format(
            individual_1_id, individual_2_id
        ))
        ind_1 = self.individuals[individual_1_id]
        ind_2 = self.individuals[individual_2_id]
        if ((ind_1.father != '0' and ind_1.father == ind_2.father) or 
            (ind_1.mother != '0' and ind_1.mother == ind_2.mother)):
            return True
        else:
            return False
    
    def check_cousins(self, individual_1_id, individual_2_id):
        """
        Check if two family members are cousins.
        
        If two individuals share any grandparents they are cousins.
        
        Arguments: 
            individual_1_id (str): The id of an individual
            individual_2_id (str): The id of an individual
        
        Returns: 
            bool : True if the individuals are cousins
                   False if they are not cousins
        
        """
        self.logger.debug("Checking if {0} and {1} are cousins".format(
            individual_1_id, individual_2_id
        ))
        
        #TODO check if any of the parents are siblings
        pass
    
    def add_individual(self, individual_object):
        """
        Add an individual to the family.
        
        Arguments:
            individual_object (Individual)
            
        """
        ind_id = individual_object.individual_id
        self.logger.debug("Adding individual {0}".format(ind_id))
        family_id = individual_object.family
        if family_id != self.family_id:
            raise PedigreeError(self.family, individual_object.individual_id,
                "Family id of individual is not the same as family id for "\
                                    "Family object!")
        else:
            self.individuals[ind_id] = individual_object
            self.logger.debug("Individual {0} added to family {1}".format(
                ind_id, family_id
            ))
        return
    
    def get_phenotype(self, individual_id):
        """
        Return the phenotype of an individual
        
        If individual does not exist return 0
        
        Arguments:
            individual_id (str): Represents the individual id
        
        Returns:
            int : Integer that represents the phenotype
        """
        phenotype = 0 # This is if unknown phenotype
        if individual_id in self.individuals:
            phenotype = self.individuals[individual_id].phenotype
        
        return phenotype
    
    def get_trios(self):
        """
        Return the trios found in family
        """
        return self.trios
    
    def to_json(self):
        """
        Return the family in json format.
        
        The family will be represented as a list with dictionarys that
        holds information for the individuals.
        
        Returns:
            list : A list with dictionaries
        """
        json_family = [self.individuals[ind].to_json() for ind in self.individuals]
        return json_family
    
    def to_ped(self, outfile=None):
        """
        Print the individuals of the family in ped format
        
        The header will be the original ped header plus all headers found in
        extra info of the individuals
        """
        
        ped_header = [
            '#FamilyID',
            'IndividualID',
            'PaternalID',
            'MaternalID', 
            'Sex',
            'Phenotype',
        ]
        
        extra_headers = [
            'InheritanceModel',
            'Proband',
            'Consultand',
            'Alive'
        ]
        
        for individual_id in self.individuals:
            individual = self.individuals[individual_id]
            for info in individual.extra_info:
                if info in extra_headers:
                    if info not in ped_header:
                        ped_header.append(info)
        
        self.logger.debug("Ped headers found: {0}".format(
            ', '.join(ped_header)
        ))
        
        if outfile:
            outfile.write('\t'.join(ped_header)+'\n')
        else:
            print('\t'.join(ped_header))
        
        for individual in self.to_json():
            ped_info = []
            ped_info.append(individual['family_id'])
            ped_info.append(individual['id'])
            ped_info.append(individual['father'])
            ped_info.append(individual['mother'])
            ped_info.append(individual['sex'])
            ped_info.append(individual['phenotype'])
            
            if len(ped_header) > 6:
                for header in ped_header[6:]:
                    ped_info.append(individual['extra_info'].get(header, '.'))
            
            if outfile:
                outfile.write('\t'.join(ped_info)+'\n')
            else:
                print('\t'.join(ped_info))
    
    def __repr__(self):
        return "Family(family_id={0}, individuals={1}, " \
                "models_of_inheritance={2}".format(
                    self.family_id, self.individuals.keys(), 
                    self.models_of_inheritance
                    )
        
    def __str__(self):
        """Print the family members of this family"""
        family = list(self.individuals.keys())
        return "\t".join(family)

