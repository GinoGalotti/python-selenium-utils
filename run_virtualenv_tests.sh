virtualenv testing_env
pip install --no-cache-dir pytest pytest-xdist selenium testingbot sauceclient

./run_tests.sh

deactivate
