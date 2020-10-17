#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

map<ll,ll> m;
ll p[100005];

ll fnd(ll x)
{
    if(p[x]==x)
        return x;
    return p[x] = fnd(p[x]);
}

void dsu_union(ll x,ll y)
{
    ll px = fnd(x);
    ll py = fnd(y);
    
    if(px==py)
        return ;
    
    if(m[px] > m[py])
    {
        m[px] += m[py];
        p[py] = px;
        m.erase(py);
    }
    else 
    {
        m[py] += m[px];
        p[px] = py;
        m.erase(px);
    }
}

int main()
{
    ll v;
    cin>>v;
    
    ll i;
    for(i=1;i<=v;i++)
        p[i] = i;
        
    for(i=1;i<=v;i++)
        m[i] = 1;
        
    ll e;
    cin>>e;
    while(e--)
    {
        ll x,y;
        cin>>x>>y;
        dsu_union(x,y);
    }
    
    //cout<<m.size()<<endl;
    
    vector<ll> vect;
    
    for(auto it : m)
    {
        if(it.second != 0)
            vect.push_back(it.second);
    }
    
    cout<<vect.size()<<endl;
    
    sort(vect.begin() , vect.end());
    
    for(auto it : vect)
        cout<<it<<" ";
    return 0;
}
