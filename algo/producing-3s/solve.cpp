#include <iostream>
#include <string>
#include <vector>

std::string solveTC(std::istream& input_stream) {
	int N;
	std::string ans = "";
	input_stream >> N;
	std::vector<int> a;
	int ai;
	for (int i = 0; i < N; i++) {
		input_stream >> ai;
		a.push_back(abs(ai) % 10);
	}
	bool dp[10];
	for (int i = 0; i < 10; i++)
		dp[i] = false;
	std::vector<int> newDP;
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
	int T;
	std::cin >> T;
	while (T--) {
		std::cout << solveTC(std::cin) << '\n';
	}
	std::cout.flush();
}