//============================================================================
// Name        : Assignment1-LP2.cpp
// Author      : Abhishek Dhanraj
// Version     :
// Copyright   : Your copyright notice
// Description : BFS and DFS on graph
//============================================================================

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Graph
{
public:
	int N;
	int M;
	vector<vector<int>> graph;
	vector<int> vis;

	Graph()
	{
		cout << "Enter Number of Nodes: ";
		cin >> N;
		cout << "Enter Number of Edges: ";
		cin >> M;
		graph.resize(N + 1);
		vis.resize(N + 1, 0);
		int u, v;
		for (int i = 0; i < M; i++)
		{
			cin >> u >> v;
			graph[u].push_back(v);
			graph[v].push_back(u);
		}
	}
	void display()
	{
		for (int i = 1; i <= N; i++)
		{
			cout << i << " : ";
			for (int j : graph[i])
			{
				cout << j << " ";
			}
			cout << endl;
		}
	}
	void dfs(int node)
	{
		cout << node << endl;
		vis[node] = 1;
		for (int neigh : graph[node])
		{
			if (!vis[neigh])
			{
				dfs(neigh);
			}
		}
	}

	void bfs(int start)
	{
		queue<int> q;
		q.push(start);
		vis[start] = 1;
		while (!q.empty())
		{
			int node = q.front();
			q.pop();
			cout << node << endl;
			for (int neigh : graph[node])
			{
				if (vis[neigh] == 0)
				{
					vis[neigh] = 1;
					q.push(neigh);
				}
			}
		}
	}
};

int main()
{
	Graph g;
	g.display();
	g.dfs(1);

	return 0;
}
/*
 7
 8
 1 2
 2 3
 2 4
 3 5
 4 5
 1 6
 6 7
 7 5
 * */
