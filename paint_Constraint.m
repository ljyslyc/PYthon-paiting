x=0:0.1:100;y=x;
[X,Y]=meshgrid(x,y);
Z=exp(X)*(4*X.^2+2*Y.^2+(X.*Y.*4) + X.*2+1);

for i =1:1001
    if 1.5+X(i)*Y(i)-X(i)-Y(i)<=0 and X(i)*Y(i)>=10 :
        X(i)=nan;
        Y(i)=nan;
        Z(i)=nan;
    end
end
surf(X,Y,Z);
colormap(jet)