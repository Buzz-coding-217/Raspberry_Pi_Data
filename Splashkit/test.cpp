// test.cpp

#include <iostream>
#include "raspi_gpio.h"
// g++ -Wall -pthread -o test test.cpp -lpigpio -lrt

namespace splashkit_lib;
    void callback(Pins pin, uint32_t level, uint32_t tick)
    {
        std::cout << "GPIO " << static_cast<int>(pin) << " changed to " << level << " at tick " << tick << std::endl;
    }

    int main()
    {
        // Initialise the GPIO
        gpio_init();
        
        // Set GPIO pin 17 as an output
        gpio_set_mode(PIN_17, OUTPUT);
        
        // Write to GPIO pin 17
        gpio_write(PIN_17, HIGH);
        uint32_t value = gpio_read(PIN_17);
        std::cout << "GPIO 17 value: " << value << std::endl;

        // Set up PWM on GPIO pin 18
        gpio_set_pwm(PIN_18, 1000, 128);

        // Set up an event handler for GPIO pin 23 state changes
        gpio_set_event_handler(PIN_23, callback);

        // Stop PWM on GPIO pin 18
        gpio_stop_pwm(PIN_18);
        // Clean up the GPIO
        gpio_cleanup();

        return 0;
    }
