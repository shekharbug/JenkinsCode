// vars/sayHello.groovy
def call(String name = 'User') {
    // This 'call' method is what Jenkins runs when you use the command
    echo "Hello, ${name}! Welcome to the Jenkins Shared Library."
    sh "date" // You can run any standard Jenkins step here
}

