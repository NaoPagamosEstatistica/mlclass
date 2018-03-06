#include <bits/stdc++.h>
#include "shoroShiro.h"
using namespace std;
int DEBUG = 0, kNeighbors, radious, kStuck;
vector<vector<int> > nb; vector<int> aux = {0, 0, 0, 0, 0, 0};

int randInt()
{
	int rr = (next() % (2*radious + 1)) - radious;
	return(rr);
}

void neighbors(vector<int> node)
{
	nb.clear();
	for (int i = 0; i < kNeighbors; i ++)
	{
		for (int j = 0; j < 6; j ++)
			aux[j] = (node[j] + randInt() + 360) % 360;
		nb.push_back(aux);
	}
}

double norm(int x)
{
	return(x / (36.0) - 5.0);
}

double simulate(int phi[], int theta[])
{
	double x, y, gain[3], r, gg;
	x = norm(phi[0]);
	y = norm(theta[0]);
	gain[0] = sin(x) + cos(y);

	x = norm(phi[1]);
	y = norm(theta[1]);
	gain[1] = y * sin(x) - x * cos(y);

	x = norm(phi[2]);
	y = norm(theta[2]);
	r = sqrt(x * x + y * y);

	gain[2] = sin(x * x + 3.0 * y * y) / (0.1 + r * r) + (x * x + 5.0 * y * y) * exp(1.0 - r * r) / 2.0;

	gg = (4.0 * gain[0] + gain[1] + 4.0 * gain[2]);
	return(gg);
}

int gain(vector<int> x)
{
	int phi[3] = {x[0], x[2], x[4]};
	int theta[3] = {x[1], x[3], x[5]};
	return(simulate(phi, theta));
}

void hillClimb(vector<int> startNode)
{
	vector<int> currNode = startNode; int stuck = 0;
	while (1)
	{
		neighbors(currNode);
		int nextEval = -(1 << 20);
		vector<int> nextNode = aux;
		for (auto x: nb)
		{
			int result = gain(x);
			if (result > nextEval)
			{
				nextNode = x;
				nextEval = result;
			}
		}
		if (DEBUG) printf("Now: %d, Best: %d\n", nextEval, gain(currNode));
		if (nextEval <= gain(currNode))
			stuck ++;
		else
		{
			stuck = 0;
			currNode = nextNode;
		}
		if (stuck == kStuck)
			break;
	}
}

int main(int argc, char **argv)
{
	s[0] = time(NULL);
	s[1] = time(NULL); rotl(2, 3); next(); next(); next();
	int phi[3], theta[3]; vector<int> start;
	for (int i = 0; i < 3; i ++)
	{
		phi[i] = atoi(argv[2*i + 1]);
		theta[i] = atoi(argv[2*i + 2]);
		//scanf("%d %d", &phi[i], &theta[i]);
		//printf("%d %d\n", phi[i], theta[i]);
	}
	double result = simulate(phi, theta);
	start = {phi[0], theta[0], phi[1], theta[1], phi[2], theta[2]};
	hillClimb(start);
	
	return(0);
}