#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
    ll n,m,k;
    cin>>n>>m>>k;
    ll mem[505],val[505];
    ll ans[505][200005];
    for(ll i=1;i<=n;i++)
        cin>>mem[i]>>val[i];
    for(ll i=0;i<=m;i++)
        ans[0][i]=0;
    for(ll i=0;i<=n;i++)
        ans[i][0]=0;
    for(ll i=1;i<=n;i++)
    {
        for(ll j=1;j<=m;j++)
        {
            if(j<val[i])
                ans[i][j]=ans[i-1][j];
            else
                ans[i][j]=max(ans[i-1][j],mem[i]+ans[i][j-val[i]]);
        }
    }
    if(ans[n][m]<k)
        cout<<"NO"<<endl;
    else
        cout<<"YES"<<" "<<ans[n][m]<<endl;
        return 0;
}
