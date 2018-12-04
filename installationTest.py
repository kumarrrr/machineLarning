import tensorflow as tf

sess =tf.Session()

hello =tf.constant("Hello from the ML Library")

print(sess.run(hello))


a = tf.constant(10)
b =tf.constant(20)

print('a+b={0}'.format(sess.run(a+b)))
