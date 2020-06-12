def Likelihood(counter_dict, theta):
    alpha, beta, gamma = theta.values()

    pos, neg = counter_dict.values()

    post_A_pos = (alpha * gamma) / (alpha * gamma + beta * (1 - gamma))
    post_B_pos = (beta * (1 - gamma)) / (alpha * gamma + beta * (1 - gamma))
    post_A_neg = ((1 - alpha) * gamma) / ((1 - alpha) * gamma + (1 - beta) * (1 - gamma))
    post_B_neg = ((1 - beta) * (1 - gamma)) / ((1 - alpha) * gamma + (1 - beta) * (1 - gamma))

    alpha_pos_ = post_A_pos * pos
    beta_pos_ = post_B_pos * pos
    gamma_A = post_A_pos * pos + post_A_neg * neg

    alpha_neg_ = post_A_neg * neg
    beta_neg_ = post_B_neg * neg
    gamma_B = post_B_pos * pos + post_B_neg * neg

    return alpha_pos_, beta_pos_, gamma_A, alpha_neg_, beta_neg_, gamma_B


def calcMaximum(pos_, neg_):
    return pos_ / (neg_ + pos_)


if __name__ == "__main__":
    counter_dict = {'pos': 6, 'neg': 4}
    theta = {'alpha': 0.5, 'beta': 0.5, 'gamma': 0.5}

    for i in range(100):
        alpha_pos_, beta_pos_, gamma_A, alpha_neg_, beta_neg_, gamma_B = Likelihood(counter_dict, theta)
        theta['alpha'] = calcMaximum(alpha_pos_, alpha_neg_)
        theta['beta'] = calcMaximum(beta_pos_, beta_neg_)
        theta['gamma'] = calcMaximum(gamma_A, gamma_B)

    print(theta)
