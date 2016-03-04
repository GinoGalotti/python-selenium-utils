rm -rf SeleniumPythonFramework/src/main/Tests/FunctionalTests/__pycache__/
rm -f SeleniumPythonFramework/src/main/Tests/FunctionalTests/*.pyc

#Init env variables if needed

#Ths is needed because of pytest http://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada
export PYTHONPATH=.
py.test SeleniumPythonFramework/src/main/Tests/FunctionalTests
