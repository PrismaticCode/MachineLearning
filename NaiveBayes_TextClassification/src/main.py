import sys
import warnings
import evaluationMetrics

warnings.filterwarnings("ignore")

# Here we take the inputs given in the command line
arguments = list(sys.argv)

data_set_name = str(arguments[1])


def main():
    """
    This is the main function which is used to run all the algorithms
    :return:
    """
    evaluation_metrics = evaluationMetrics.evaluate_multinomial_NB(data_set_name)
    print("The accuracy is", evaluation_metrics[0])
    print("The Precision is", evaluation_metrics[1])
    print("The Recall is", evaluation_metrics[2])
    print("The F1 Score is", evaluation_metrics[3])


if __name__ == "__main__":
    main()
