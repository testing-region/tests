function [theta, J_history] = grad(X, y, theta, alpha, num_iters)
%GRADIENTDESCENTMULTI Performs gradient descent to learn theta
%   theta = GRADIENTDESCENTMULTI(x, y, theta, alpha, num_iters) updates theta by
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);

for iter = 1:num_iters

    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCostMulti) and gradient here.
    %


    h = X * theta;
    sh = h - y;
    sh1 = sum(sh);
    sh2 = sum(sh .* X(:,2));
    sh3 = sum(sh .* X(:,3));
    
    theta(1) = theta(1) - (alpha * (1/m) * sh1);
    theta(2) = theta(2) - (alpha * (1/m) * sh2);
    theta(3) = theta(3) - (alpha * (1/m) * sh3);


    % ============================================================

    % Save the cost J in every iteration    
    J_history(iter) = cost(X, y, theta);

end

end

