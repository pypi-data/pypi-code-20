import os
import nose
import shutil
import yaml
from sherlock.utKit import utKit

from fundamentals import tools

su = tools(
    arguments={"settingsFile": None},
    docString=__doc__,
    logLevel="DEBUG",
    options_first=False,
    projectName="sherlock"
)
arguments, settings, log, dbConn = su.setup()

# # load settings
# stream = file(
#     "/Users/Dave/.config/sherlock/sherlock.yaml", 'r')
# settings = yaml.load(stream)
# stream.close()

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()

# load settings
stream = file(
    pathToInputDir + "/example_settings.yaml", 'r')
settings = yaml.load(stream)
stream.close()

import shutil
try:
    shutil.rmtree(pathToOutputDir)
except:
    pass
# COPY INPUT TO OUTPUT DIR
shutil.copytree(pathToInputDir, pathToOutputDir)

# Recursively create missing directories
if not os.path.exists(pathToOutputDir):
    os.makedirs(pathToOutputDir)

# xt-setup-unit-testing-files-and-folders


# class test_update_wiki_pages(unittest.TestCase):

#     def test_update_wiki_pages_function(self):

#         from sherlock.commonutils import update_wiki_pages
#         wiki = update_wiki_pages(
#             log=log,
#             settings=settings
#         )
#         wiki.update()

#     def test_update_wiki_pages_function_exception(self):

#         from sherlock.commonutils import update_wiki_pages
#         try:
#             this = update_wiki_pages(
#                 log=log,
#                 settings=settings,
#                 fakeKey="break the code"
#             )
#             this.update()
#             assert False
#         except Exception, e:
#             assert True
#             print str(e)

    # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
