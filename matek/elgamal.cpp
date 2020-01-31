#include <iostream>

int linkong(int r0, int r1)
{
  int x0=1,x1=0,p=r1;
  while(r1!=0)
  {
    int q1=r0/r1;
    int r2=r0-r1*q1;
    r0=r1; r1=r2;

    int x=x0;
    x0=x1;
    x1=x-q1*x1;
  }
  if(x0<0)
  {
    x0+=(-x0/p+1)*p;
  }

  return x0;
}

int gyorshatvany(int x, int n, int m)
{
  int hatvanyok[32];
  hatvanyok[0]=1;
  for(int i=1; i<32; i++)
  {
    hatvanyok[i]=x % m;
    x=hatvanyok[i]*hatvanyok[i];
  }

  int eredmeny=1;
  unsigned int mask = 1U<<(31);
  for(int i=0; i<32; i++)
  {
    int val=(n&mask) ? hatvanyok[32-i] : 1;
    eredmeny*=val;
    n<<=1;
  }
  return eredmeny%m;
}

struct Uzike
{
  Uzike():mhy(0),gy(0){}
  Uzike(int mhy_, int gy_):mhy(mhy_),gy(gy_) {}
  int mhy, gy;
};

Uzike titkosit(char c, int y, int h, int g, int n)
{
  int m=c-96;

  int hy=gyorshatvany(h,y,n);
  int mhy=m*hy % n;
  int gy=gyorshatvany(g,y,n);

  return Uzike(mhy,gy);
}

char dekodol(Uzike u, int x, int n)
{

  int c2x=gyorshatvany(u.gy,x,n);
  int inv = linkong(c2x,n);
  int dek=u.mhy*inv % n;

  char cucc = dek + 96;
  return cucc;
}

int main()
{
  int g=2, x=5, n=29, y=2;
  int h=gyorshatvany(g,x,n);

  std::string be;
  std::cin>>be;
  int hossz = be.length();

  Uzike u[hossz];

  for(int i=0; i<hossz; i++)
  {
    u[i]=titkosit(be[i],y,h,g,n);
    std::cout<<u[i].mhy<<u[i].gy;
  }
  std::cout<<std::endl;

  for(int i=0; i<hossz; i++)
  {
    std::cout<<dekodol(u[i],x,n);
  }
  std::cout<<std::endl;

  return 0;
}
