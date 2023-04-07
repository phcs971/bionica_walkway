from entities.study import Study
import matplotlib.pyplot as plt

class PlotHelper:
    @staticmethod 
    def plot_studies(studies, use_subplots=False):
        if (use_subplots):
            fig, axes = plt.subplots(len(studies), 1)
            for i, study in enumerate(studies):
                ax = axes[i]
                study.plot(ax)
                ax.set_aspect('equal', 'box')
                ax.set_ylim(0, 50)
                ax.set_title(str(study))
        else: 
            colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'gray', 'olive', 'cyan']
            fig, ax = plt.subplots()
            for i, study in enumerate(studies):
                study.plot(ax, color=colors[i])
                # ax.legend()
                ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.5))
                # ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

            ax.set_aspect('equal', 'box')
            ax.set_ylim(0, 50)
        plt.show()

