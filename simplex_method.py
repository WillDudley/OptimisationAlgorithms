import numpy as np

# The Simplex Method is an algorithm to minimise or maximise a condition subject to constraints.


class SimplexMethod:

    def __init__(self):
        self.profit = []
        self.total_resources = []
        self.resources_cost = None
        self.number_of_products = 0
        self.number_of_resources = 0
        self.tableau = None
        self.maximise = None

    # ### Collect Data ###
    # enter number of products
    # enter number of resources
    # enter profit for each product
    # enter total number of resources for each resource
    # enter resources cost for each product

    def collect_data(self):
        self.number_of_products = int(input('Enter number of different products: '))
        self.number_of_resources = int(input('Enter number of different resources: '))

        max_or_min = int(input('Maximise or minimise profit? Enter 1 for maximise or 2 for minimize: '))
        while max_or_min != 1 | max_or_min != 2:
            max_or_min = int(input('Please enter a valid option: '))
        if max_or_min == 1:
            self.maximise = True
        elif max_or_min == 2:
            self.maximise = False
        else:
            raise NameError('self.Maximum assignment error.')

        # profit = []
        for i in range(self.number_of_products):
            self.profit.append(float(input('Enter profit for product ' + str(i+1) + ': ')))

        # total_resources = []
        for i in range(self.number_of_resources):
            self.total_resources.append(float(input('Enter total number of resources for resource ' + str(i+1) + ': ')))

        self.resources_cost = np.zeros(shape=(self.number_of_products, self.number_of_resources))
        for j in range(self.number_of_resources):
            for i in range(self.number_of_products):
                self.resources_cost[i][j] = float(input('Enter resource ' + str(j+1) + ' cost for product ' + str(i+1) + ': '))

    # ###Print Problem###
    # print maximise/minimise
    # print LC of profit/product
    # print LC of resource_cost/resource <= total resource

    def print_problem(self):

        print('--------------------------------------------------------------')

        objective_function = ''
        for i in range(self.number_of_products):
            objective_function + str(self.profit[i]) + ' x_' + str(i) + ' + '
        objective_function = objective_function[:-3]

        if self.maximise:
            print('Maximise: ' + objective_function)
        else:
            print('Minimise: ' + objective_function)

        print('Subject to the following constraints: ')

        for i in range(self.number_of_resources):
            constraint = ''
            for j in range(self.number_of_products):
                constraint + str(self.resources_cost[i][j]) + ' x_' + str(i) + ' + '
            constraint = constraint[:-3] + ' <= ' + str(self.total_resources[i])
            print(constraint)

        print('Where all x_i >= 0')

        print('--------------------------------------------------------------')

    # ###Generate Tableau###
    # Introduce slack variables
    # Print tableau

    def generate_tableau(self):
        self.tableau = np.zeros(shape=(self.number_of_resources + 1, (self.number_of_products * 2) + 1))

        for i in range(self.number_of_resources):
            self.tableau[i][0] = self.total_resources[i]
            for j in range(self.number_of_products):
                self.tableau[i][1+j] = self.resources_cost[i][j]
            # for j in range(self.number_of_resources, self.number_of_resources*2):
            #     if i == j:
            #         self.tableau[i][self.number_of_resources+1+j] = 1
            self.tableau[i][self.number_of_resources + 1 + i] = 1

        if self.maximise:
            for j in range(self.number_of_products):
                self.tableau[-1][1+j] = -1 * self.profit[j]
        else:
            for j in range(self.number_of_products):
                self.tableau[-1][1+j] = self.profit[j]

        print(self.tableau)


if __name__ == "__main__":
    Problem = SimplexMethod()
    Problem.collect_data()
    Problem.print_problem()
    Problem.generate_tableau()
