% Problem #65 
% This problem was asked by Amazon.
% 
% Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
% 
% For example, given the following matrix:
% 
% [[1,  2,  3,  4,  5],
%  [6,  7,  8,  9,  10],
%  [11, 12, 13, 14, 15],
%  [16, 17, 18, 19, 20]]
% You should print out the following:
% 
% 1
% 2
% 3
% 4
% 5
% 10
% 15
% 20
% 19
% 18
% 17
% 16
% 11
% 6
% 7
% 8
% 9
% 14
% 13
% 12

clear;
itermax=160;alpha=8;min=itermax-9;
for beta=-1:0.001:1
x=0;
xo=x;
for n=1:itermax
xn=exp(-alpha*xo^2)+beta;
x=[x xn];
xo=xn;
end
plot(beta*ones(10),x(min:itermax),'.','MarkerSize',1)
hold on
end
fsize=15;
set(gca,'xtick',[-1:0.5:1],'FontSize',fsize)
set(gca,'ytick',[-1:0.5:1],'FontSize',fsize)
xlabel('{\beta}','FontSize',fsize)
ylabel('\itx','FontSize',fsize)
hold off