#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

// used to solve
vector<vector<int>> adj;
vector<bool> vis;
vector<int> comp;
bool deg3, deg1, flag;
int deg3n, deg1n;

void dfs(int s) {
	vis[s] = true;
	comp.push_back(s);

	if (adj[s].size() == 1) {
		if (deg1)
			flag = false;
		else {
			deg1 = true;
			deg1n = s;
		}
	}
	if (adj[s].size() == 3) {
		if (deg3)
			flag = false;
		else {
			deg3 = true;
			deg3n = s;
		}
	}
	if (adj[s].size() == 0 || adj[s].size() > 3)
		flag = false;

	for (int v : adj[s]) {
		if (!vis[v])
			dfs(v);
	}
}

int pr = -1;
int findLength(int s, int g) {
	if (s == g)
		return 0;

	for (int v : adj[s]) {
		if (v != pr) {
			pr = s;
			return 1 + findLength(v, g);
		}
	}

	return -1;
}

// solve test case
int solveTC(istream& input_stream) {
	int ans = 0;
	int N, M;
	input_stream >> N >> M;
	adj.clear();
	adj.resize(N);
	vis.clear();
	vis.resize(N);
	int ui, vi;

	for (int i = 0; i < M; i++) {
		input_stream >> ui >> vi;
		ui--;
		vi--;
		adj[ui].push_back(vi);
		adj[vi].push_back(ui);
	}

	int l;
	for (int i = 0; i < N; i++) {
		if (vis[i])
			continue;
		comp.clear();
		deg3 = false;
		deg1 = false;
		flag = true;
		deg3n = -1;
		deg1n = -1;
		pr = -1;
		dfs(i);
		if (flag && deg3 && deg1) {
			l = findLength(deg1n, deg3n);
			int compSize = comp.size();

			if ((compSize - l) % 4 == 0 && l > 0)
				ans = max((compSize - l) * (compSize - l) + l, ans);
		}
	}

	return ans;
}

vector<pair<int, int>> connections;
int nodesUsed = 0;
int edgesUsed = 0;
int fSize = 0;
int pSize = 0;
vector<int> nodes;
void genTC(ostream& out_stream, int c, int f, int ms) {
    srand(time(0));
	bool flags[c];
	for (int i = 0; i < c; i++)
		flags[i] = false;
	int randomFlag;
	for (int i = 0; i < f; i++) {
		randomFlag = rand() % c;
		if (flags[randomFlag]) {
			i--;
		} else
			flags[randomFlag] = true;
	}

	for (bool b : flags) {
		if (b) {
			fSize = (rand() % ((ms - 1) / 4) + 1) * 4;
			pSize = (rand() % (ms - fSize) + 1);
			for (int i = 0; i < fSize; i++)
				nodes.push_back(i + nodesUsed + 1);
			random_shuffle(nodes.begin(), nodes.end());
			for (int i = 0; i < fSize - 1; i++)
				connections.push_back({nodes[i], nodes[i + 1]});
			connections.push_back({nodes[fSize - 1], nodes[0]});
			nodesUsed += fSize;
			nodes.clear();

			for (int i = 0; i < pSize; i++)
				nodes.push_back(i + nodesUsed + 1);
			random_shuffle(nodes.begin(), nodes.end());
			for (int i = 0; i < pSize - 1; i++)
				connections.push_back({nodes[i], nodes[i + 1]});
			connections.push_back({nodesUsed, nodes[0]});
			nodes.clear();
			nodesUsed += pSize;
			edgesUsed += pSize + fSize;
		} else {
			fSize = (rand() % ms + 1);
			for (int i = 0; i < fSize; i++) {
				for (int j = i + 1; j < fSize; j++) {
					if (rand() % 3 == 1) {
						connections.push_back({i + nodesUsed + 1, j + nodesUsed + 1});
						edgesUsed++;
					}
				}
			}
			nodesUsed += fSize;
		}
	}
	out_stream << nodesUsed << " " << edgesUsed << endl;
	for (pair<int, int> p : connections)
		out_stream << p.first << " " << p.second << endl;
	connections.clear();
	nodesUsed = 0;
	edgesUsed = 0;
	fSize = 0;
	pSize = 0;
}

int main() {
	ios_base::sync_with_stdio(false);
	// generate test cases
	ostringstream out_stream;
	out_stream << 41 << endl;
	out_stream << "17 17" << endl
			   << "1 2" << endl
			   << "2 3" << endl
			   << "3 4" << endl
			   << "4 1" << endl
			   << "1 5" << endl
			   << "5 6" << endl
			   << "7 8" << endl
			   << "8 9" << endl
			   << "9 10" << endl
			   << "10 11" << endl
			   << "11 12" << endl
			   << "12 13" << endl
			   << "13 9" << endl
			   << "14 15" << endl
			   << "15 16" << endl
			   << "16 17" << endl
			   << "17 14" << endl;

	for (int i = 0; i < 20; i++) {
		genTC(out_stream, 10, rand() % 10 + 1, 100);
	}

	for (int i = 0; i < 20; i++) {
		genTC(out_stream, 100, rand() % 100 + 1, 20);
	}

	string input = out_stream.str();
	istringstream input_stream(input);
	// create solutions
	int T;
	input_stream >> T;
	vector<int> ans;
	while (T--)
		ans.push_back(solveTC(input_stream));

	// check solutions
	cout << input << '\n';
	cout << "Output:" << endl;

	bool correct = true;
	int ans2;
	for (int i : ans) {
		cin >> ans2;
		if (ans2 != i)
			correct = false;
	}

	if (!correct)
		cout << "Sorry, you did not get the correct output" << endl;
	else
		cout << "flag{l4rge_fl4g_4738}" << endl;
}
