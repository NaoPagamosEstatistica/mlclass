#include <bits/stdc++.h>

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

int main(int argc, char **argv)
{
	int phi[3], theta[3];
	for (int i = 0; i < 3; i ++)
	{
		phi[i] = atoi(argv[2*i + 1]);
		theta[i] = atoi(argv[2*i + 2]);
		//scanf("%d %d", &phi[i], &theta[i]);
	}
	double result = simulate(phi, theta);
	printf("%.20lg\n", result);

	return(0);
}