import math
import matplotlib.pyplot as plt

p = 53
base = 2

def modexp( base, exp, p ):
    return ( base ** exp ) % p

def dlog( y, base, p ):
    for i in range( 1, p ):
        if modexp( base, i, p ) == y:
            return i

def plot_dlogs():
    x = [ i for i in range( 1, p ) ]

    def dlog_spec( x ):
        return dlog( x, base, p )

    y = map( dlog_spec, x )
    plt.plot( x, y )
    plt.title( "x vs. log2(x) mod 53")
    plt.xlabel( "x" )
    plt.ylabel( "discrete logarithm of x with base = 2, n = 53" )
    plt.show()

def plot_logs():
    x = [ i for i in range( 1, p ) ]

    def log( x ):
        return math.log( x, 2 )

    y = map( log, x )
    plt.plot( x, y )
    plt.title( "x vs. log2(x)")
    plt.xlabel( "x" )
    plt.ylabel( "logarithm of x with base = 2" )
    plt.show()

if __name__ == "__main__":
    plot_dlogs()
    plot_logs()
