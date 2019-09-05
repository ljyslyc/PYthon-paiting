clear;clc;

figure(2);

x0 = [-3:0.02:12.1];
y0 = [4.1:0.02:5.8]
% z0 = 21.5 + x0.*sin(4*pi*x0)+y0.*sin(20*pi*y0);
%% 重构三维数据，画图
%间隔为 0.05的时候，X Y数据为 *****×****，  电脑一般的，将间隔调大
%间隔为    1的时候，X Y数据为 ***×****，    电脑  好的，将间隔调小
[X,Y]=meshgrid(x0,y0);%将x、y轴网格化，重构用于画图x、y轴数据
Z= 21.5 + X.*sin(4*pi*X)+Y.*sin(20*pi*Y);
%griddata(xRow,yCol,z,X,Y);%插值，重构用于画图的Z轴数据
mesh(X,Y,Z, 'EdgeColor', [0,0,0])
