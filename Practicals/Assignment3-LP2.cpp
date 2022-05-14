//============================================================================
// Name        : Assignment3-LP2.cpp
// Author      : Abhishek Dhanraj
// Version     :
// Copyright   : Your copyright notice
// Description : Single source shortest path
//============================================================================

#include <bits/stdc++.h>
using namespace std;

int N, M;
vector<vector<pair<int, int>>> graph;
int dist[10];

void Dijkstra(int start)
{
	set<pair<int, int>> pq;
	pq.insert({0, start});
	dist[start] = 0;
	while (pq.size())
	{
		auto it = pq.begin();
		int node = it->second;
		cout << node << endl;
		pq.erase(it);
		for (auto neigh : graph[node])
		{
			if (neigh.second + dist[node] < dist[neigh.first])
			{
				dist[neigh.first] = dist[node] + neigh.second;
				pair<int, int> p = {dist[neigh.first], neigh.first};
				pq.insert(p);
			}
		}
	}
}

void display()
{
	for (int i = 1; i <= N; i++)
	{
		cout << i << " : ";
		for (auto j : graph[i])
		{
			cout << (j.first) << " " << (j.second) << "\t";
		}
		cout << endl;
	}
}
int main()
{
	cout << "Enter Number of Nodes: ";
	cin >> N;
	cout << "Enter Number of Edges: ";
	cin >> M;
	graph.resize(N + 1);
	int u, v, w;
	for (int i = 0; i < M; i++)
	{
		cin >> u >> v >> w;
		graph[u].push_back({v, w});
		graph[v].push_back({u, w});
	}
	display();
	for (int i = 0; i <= N; ++i)
	{
		dist[i] = INT_MAX;
	}
	Dijkstra(1);
	for (int i = 0; i <= N; ++i)
	{
		cout << i << " : " << dist[i] << endl;
	}
	return 0;
}
/*
 7
 8
 1 2 1
 2 3 2
 2 4 3
 3 5 4
 4 5 5
 1 6 6
 6 7 7
 7 5 8

 */
