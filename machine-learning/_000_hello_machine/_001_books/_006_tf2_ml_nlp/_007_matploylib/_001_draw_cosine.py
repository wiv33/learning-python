import matplotlib.pylab as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 128)
y = np.cos(x)
print(y)
# [-1.         -0.99877642 -0.99510866 -0.9890057  -0.98048249 -0.96955986
#  -0.95626457 -0.94062913 -0.92269182 -0.90249652 -0.88009266 -0.85553507
#  -0.82888384 -0.8002042  -0.76956632 -0.73704518 -0.70272037 -0.66667589
#  -0.62899993 -0.58978471 -0.54912619 -0.50712386 -0.46388052 -0.41950198
#  -0.37409685 -0.32777625 -0.28065352 -0.23284398 -0.18446464 -0.13563388
#  -0.0864712  -0.03709691  0.01236816  0.06180296  0.11108653  0.16009824
#   0.20871817  0.25682733  0.30430798  0.35104395  0.39692085  0.44182643
#   0.48565077  0.52828665  0.56962973  0.60957882  0.64803617  0.68490767
#   0.72010309  0.75353629  0.78512546  0.8147933   0.84246721  0.86807945
#   0.89156736  0.91287345  0.93194559  0.94873711  0.9632069   0.97531957
#   0.98504546  0.99236079  0.99724764  0.99969406  0.99969406  0.99724764
#   0.99236079  0.98504546  0.97531957  0.9632069   0.94873711  0.93194559
#   0.91287345  0.89156736  0.86807945  0.84246721  0.8147933   0.78512546
#   0.75353629  0.72010309  0.68490767  0.64803617  0.60957882  0.56962973
#   0.52828665  0.48565077  0.44182643  0.39692085  0.35104395  0.30430798
#   0.25682733  0.20871817  0.16009824  0.11108653  0.06180296  0.01236816
#  -0.03709691 -0.0864712  -0.13563388 -0.18446464 -0.23284398 -0.28065352
#  -0.32777625 -0.37409685 -0.41950198 -0.46388052 -0.50712386 -0.54912619
#  -0.58978471 -0.62899993 -0.66667589 -0.70272037 -0.73704518 -0.76956632
#  -0.8002042  -0.82888384 -0.85553507 -0.88009266 -0.90249652 -0.92269182
#  -0.94062913 -0.95626457 -0.96955986 -0.98048249 -0.9890057  -0.99510866
#  -0.99877642 -1.        ]

plt.plot(y)
plt.show()
