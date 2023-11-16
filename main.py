import mock, sys, logger, os, pathlib 
mock_data = mock.mock_dict()

if len(sys.argv) < 2:
	print("expected arguments: '-print', '-logging', '-clean'")

if "-print" in sys.argv:
	print("username\t" + mock_data['username'])
	print("email   \t" + mock_data['email'])
	print("password\t" + mock_data['password'])
	print("job     \t" + mock_data['job'])
	print("name    \t" + mock_data['name'])
	print("birth   \t" + mock_data['date_of_birth'])
	print("passport\t" + mock_data['passport_num'])
	print("expiry  \t" + mock_data['passport_exp'])
	print("\n")

if "-clean" in sys.argv:
	paths = pathlib.Path(os.getcwd()).glob('*.json')

	for path in paths:
		path.unlink()

if "-log" in sys.argv:
	logger.write(mock_data)
