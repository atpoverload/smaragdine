# build rust code
cargo build --release

# build python client
pip install . -r requirements.txt

# run the server
COMMAND="target/release/smaragdine"
sudo "${COMMAND}" &
sleep 1

# smoke test the clients
target/release/client smoke_test

SMOKE_TEST_DATA="smoke-test.json"
rm "${SMOKE_TEST_DATA}"
python3 -m smaragdine.client start --pid 1
sleep 1
python3 -m smaragdine.client stop
python3 -m smaragdine.client read > "${SMOKE_TEST_DATA}"
wc -l "${SMOKE_TEST_DATA}"

# smoke test the tf hook
TEMP_DIR="/tmp/smaragdine"
rm -rf "${TEMP_DIR}"
mkdir -f "${TEMP_DIR}"
python3 smoke_test.py
ls -l $TEMP_DIR/*

# kill the server by grabbing the smaragdine pids
pids=$(ps -ef | grep "${COMMAND}" | awk '{print $2}')
sudo kill -9 ${pids}
