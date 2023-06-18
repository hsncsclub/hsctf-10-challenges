#include <iostream>
#include <vector>
#include <string>
#include <stdlib.h>
#include <time.h>
#include <map>
#include <climits>

using namespace std;

const int N = 10;
const int K = N*N;
const int T = N*(N+1)/2;
const int M = 27;

struct Sub{
	int pa;
	int rk;
};

int find(vector<Sub>& DSU, int a){
	return (DSU[a].pa == a ? a : DSU[a].pa = find(DSU, DSU[a].pa));
}

void Union(vector<Sub>& DSU, int a, int b){
	a = find(DSU, a);
	b = find(DSU, b);
	if(a == b) return;
	if(DSU[a].rk > DSU[b].rk) DSU[b].pa = a;
	else if(DSU[a].rk < DSU[b].rk) DSU[a].pa = b;
	else{
		DSU[b].pa = a;
		DSU[a].rk ++;
	}
}

void clean(string& edges, int v){
	vector<Sub> DSU(N);
	for(int i = 0; i < N; i ++){
		DSU[i].pa = i;
		DSU[i].rk = 1;
	}

	for(int i = 0; i < K; i ++){
		if(edges[i] == '1'){
			Union(DSU, i/N, i%N);
		}
	}
	for(int i = 0; i < K; i ++){
		if(edges[i] == '1'){
			if(find(DSU, i/N) != find(DSU, v))
				edges[i] = '0';
		}
	}
}

map<pair<string, int>, pair<int, int> > dp;

int solve(string edges, int v){
	if(dp.size() > 5000000) return -1;
	clean(edges, v);
	if(dp.find({edges, v}) != dp.end() && dp[{edges, v}] != make_pair(0, 0))
		return dp[{edges, v}].first;
	
	int best = -1;
	int next = -1;
	for(int i = 0; i < N; i ++){
		int a = min(i, v); int b = max(i, v);
		if(edges[N*a + b] == '0') continue;
		edges[N*a + b] = '0';
		int u = solve(edges, i);
		edges[N*a + b] = '1';
		if(u < 0 && -u >= best){
			best = -u + 1;
			next = i;
		}
		else if(u > 0 && best < 0 && u >= -best){
			best = -u - 1;
			next = i;
		}
		if(best > 0) break;
	}
	dp[{edges, v}] = {best, next};
	return best;
}

int main(){
	string flag = "flag{d0m1n0_th30ry_4005ca}";
	
	for(int t = 0; t < 6; t ++){
		srand(time(NULL));
		string edges = "";
		for(int i = 0; i < K; i ++) edges += '0';
		int count = 0;
		int u = 1;
		for(int i = 0; i < N; i ++){
			for(int j = i; j < N; j ++){
				if(i == 0 && j == 0) continue;
				//guaranteed generation of M dominos
				if((rand() % (T - u)) < (M - count)){ 
					count ++;
					edges[N*i + j] = '1';
				}
				u++;
			}
		}
		cout << count << endl;
		for(int i = 0; i < N; i ++){
			for(int j = i; j < N; j ++){
				if(edges[N*i + j] == '1') cout << i << " " << j << endl;
			}
		}
		
		solve(edges, 0);
		cout << endl;
		//cout << solve(edges, 0) << endl;
		//cout << dp.size() << endl;
		
		int cur = 0;
		bool first = true;
		while(1){
			clean(edges, cur);
			solve(edges, cur);
			//cout << dp[{edges, cur}].first << endl;
			//force player to have a win
			if(first && dp[{edges,cur}].first > 0) cout << "0 0" << endl;
			else{
				int next = dp[{edges, cur}].second;
				if(next == -1){
					cout << "you win" << endl;
					break;
				}
				cout << cur << " " << next << endl;
				edges[N*min(cur, next) + max(cur,next)] = '0';
				cur = next;
			}
			int u, v;
			cin >> u >> v;
			if(u != cur && v != cur){
				cout << "Bad Input" << endl;
				return 0;
			}
			if(edges[N*min(u,v) + max(u,v)] == '0'){
				cout << "Bad Input" << endl;
				return 0;
			}
			edges[N*min(u,v) + max(u,v)] = '0';
			cur = u + v - cur;
			first = false;
		}
	}
	cout << flag << endl;


	return 0;
}

