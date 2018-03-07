#include <bits/stdc++.h>
#include "shoroShiro.h"
using namespace std;
int DEBUG = 0, kNeighbors, radious, kStuck;
vector<vector<int> > nb; vector<int> aux = {0, 0, 0, 0, 0, 0};

void printVector(vector<int> a)
{
	for (int i = 0; i < 6; i ++)
		printf("%d%s", a[i], i < 6 - 1 ? " " : "\0");
}

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

double gain(vector<int> x)
{
	int phi[3] = {x[0], x[2], x[4]};
	int theta[3] = {x[1], x[3], x[5]};
	return(simulate(phi, theta));
}

vector<int> hillClimb(vector<int> startNode)
{
	vector<int> currNode = startNode; int stuck = 0;
	while (1)
	{
		neighbors(currNode);
		double nextEval = -(1 << 20);
		vector<int> nextNode = aux;
		for (auto x: nb)
		{
			double result = gain(x);
			if (result > nextEval)
			{
				nextNode = x;
				nextEval = result;
			}
		}
		if (DEBUG)
		{
			printf("Now: %.20lg <- ", nextEval);
			printVector(nextNode);
			printf("; Best: %.20lg <- ", gain(currNode));
			printVector(currNode); printf("\n");
		}
		if (nextEval <= gain(currNode))
			stuck ++;
		else
		{
			stuck = 0;
			currNode = nextNode;
		}
		if (stuck == kStuck)
			return(currNode);
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
	DEBUG = atoi(argv[7]);
	kNeighbors = atoi(argv[8]);
	radious = atoi(argv[9]);
	kStuck = atoi(argv[10]);
	//double result = simulate(phi, theta);
	start = {phi[0], theta[0], phi[1], theta[1], phi[2], theta[2]};
	vector<int> ans = hillClimb(start);
<<<<<<< HEAD
	printVector(ans); printf(" -> %.20lg\n", gain(ans));
=======
	printf("%.20lg -> ", gain(ans)); printVector(ans); printf("\n");
>>>>>>> cc7791fb0c354a759702f3448a3bec3b4b068a95

	return(0);
}