X = [1 2; 1 3; 1 4];
y = [7;9;11];
m = 3;
theta = [0;0];
A = X(:,2);

for i = [1:18000]

h = X * theta;
sh = h - y;
sh1 = sum(sh);
sh2 = sum(sh .* A);

theta(1) = theta(1) - (0.01 * (1/m) * sh1);
theta(2) = theta(2) - (0.01 * (1/m) * sh2);

disp(theta);
disp(' ');

endfor
