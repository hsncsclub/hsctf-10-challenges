#include <cstdlib>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

int solveTC(istream& input_stream) {
	int N, sum = 0, m = 0;
	input_stream >> N;
	vector<int> arr(N);
	vector<int> prefix(N);
	for (int x = 0; x < N; x++) {
		input_stream >> arr[x];
		sum += arr[x];
		prefix[x] = sum;
	}

	for (int x = 0; x < N; x++) {
		for (int y = x; y < N; y++) {
			if (x != 0 && (prefix[y] - prefix[x - 1]) % (y - x + 1) == 0) {
				m = max(m, y - x + 1);
			} else if (x == 0 && prefix[y] % (y + 1) == 0) {
				m = max(m, y + 1);
			}
		}
	}
	return m;
}

int main() {
	ios_base::sync_with_stdio(false);
	ostringstream out_stream;

	out_stream << 1000 << endl;
	for (int i = 0; i < 1000; i++) {
		out_stream << (rand() % (1000 - 1 + 1)) + 1 << " ";
	}

	string input = out_stream.str();
	istringstream input_stream(input);
	int ans = solveTC(input_stream);

	// check solutions
	cout << input << '\n';
	cout << "Output:" << endl;

	int userAns;
	cin >> userAns;

	if (userAns != ans)
		cout << "Sorry, you did not get the correct output" << endl;
	else
		cout << "flag{j3k4m4_2n1_3m}" << endl;
}
