#include <climits>
#include <cstdlib>
#include <iostream>
#include <random>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

// solve test case
string solveTC(istream& input_stream) {
	int N;
	string ans = "";
	input_stream >> N;
	vector<int> a;
	int ai;
	for (int i = 0; i < N; i++) {
		input_stream >> ai;
		a.push_back(abs(ai) % 10);
	}
	bool dp[10];
	for (int i = 0; i < 10; i++)
		dp[i] = false;
	vector<int> newDP;
	bool added = false;
	for (int i : a) {
		if (i == 3) {
			ans += "Y";
			added = true;
		}
		newDP.push_back(i);
		for (int j = 0; j < 10; j++) {
			if (dp[j]) {
				newDP.push_back((j * i) % 10);
				if (!added && (j * i) % 10 == 3) {
					ans += "Y";
					added = true;
				}
			}
		}
		if (!added)
			ans += "N";
		for (int j : newDP)
			dp[j] = true;
		newDP.clear();
		added = false;
	}

	return ans;
}

int main() {
	ios_base::sync_with_stdio(false);
	// generate test cases
	random_device rd;
	default_random_engine mt(rd());
	uniform_int_distribution<int> dist(0, INT_MAX);
	uniform_int_distribution<int> dist2(0, 1000);

	ostringstream out_stream;
	out_stream << 801 << '\n';
	for (int i = 0; i < 200; i++) {
		out_stream << 10 << '\n';
		for (int j = 0; j < 10; j++)
			out_stream << dist(mt) << " ";

		out_stream << '\n';
	}
	for (int i = 0; i < 200; i++) {
		out_stream << 100 << '\n';
		for (int j = 0; j < 100; j++)
			out_stream << dist(mt) << " ";

		out_stream << '\n';
	}
	for (int i = 0; i < 200; i++) {
		out_stream << 1000 << '\n';
		for (int j = 0; j < 1000; j++)
			out_stream << dist(mt) << " ";

		out_stream << '\n';
	}
	for (int i = 0; i < 200; i++) {
		int r = dist2(mt);
		out_stream << r << '\n';
		for (int j = 0; j < r; j++)
			out_stream << (dist(mt) * dist(mt) / 2) - 268419073 << " ";

		out_stream << '\n';
	}

	out_stream << 10000 << '\n';
	for (int j = 0; j < 10000; j++)
		out_stream << (dist(mt) - 16383) << " ";

	out_stream << endl;
	string input = out_stream.str();

	// create solutions
	istringstream input_stream(input);
	int T;
	input_stream >> T;
	vector<string> ans;
	while (T--)
		ans.push_back(solveTC(input_stream));

	// check solutions
	cout << input << '\n';
	cout << "Output: " << endl;

	bool correct = true;
	string s2;
	for (const string& s : ans) {
		cin >> s2;
		if (s != s2) {
			correct = false;
			break;
		}
	}
	if (!correct)
		cout << "Sorry, you did not get the correct output" << '\n';
	else
		cout << "flag{n1c3_w0rk_8329}" << '\n';
}
