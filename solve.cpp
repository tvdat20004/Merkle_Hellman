#include <bits/stdc++.h>
#define ll long long
using namespace std;
ll s[] = {184, 332, 713, 1255, 2688, 5243, 10448};
int main()
{
	ll k[] = {10632, 15875, 16588, 15875,18175,13320,3733,7727,12600,20531,897,16736,184,7727,12932,15620};
	for (int i = 0; i < 16; ++i)
	{
		bool ans[7] = {};
		for (int j = 6; j >= 0; --j)
		{
			if (k[i] >= s[j])
			{
				k[i] -= s[j];
				ans[j] = 1;
				if (k[i] == 0) break;
			} 
		}
		for (int t = 0; t < 7; ++t)
		{
			cout<<ans[t];
		}
		cout<<' ';
	}
	return 0;
}