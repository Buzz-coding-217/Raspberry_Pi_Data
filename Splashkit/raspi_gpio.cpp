// raspi_gpio.c

#include "raspi_gpio.h"
#include "pigpio.h"
#include <stdexcept>
#include <string>

namespace splashkit_lib
{

    int get_pin_number(Pins pin)
    {
        if (pin == Pins::PIN_1 || pin == Pins::PIN_2 || pin == Pins::PIN_4 || pin == Pins::PIN_17)
        {
            throw std::runtime_error("Cannot modify power pin. Pin: " + std::to_string(static_cast<uint8_t>(pin)));
        }
        if (pin == Pins::PIN_6 || pin == Pins::PIN_9 || pin == Pins::PIN_14 || pin == Pins::PIN_20 ||
            pin == Pins::PIN_25 || pin == Pins::PIN_30 || pin == Pins::PIN_34 || pin == Pins::PIN_39)
        {
            throw std::runtime_error("Cannot modify ground pin. Pin: " + std::to_string(static_cast<uint8_t>(pin)));
        }
        return static_cast<uint8_t>(pin);
    }
    void gpio_init()
    {
        gpioInitialise();
    }

    void gpio_set_mode(Pins pin, PinMode mode)
    {
        gpioSetMode(get_pin_number(pin), static_cast<uint8_t>(mode));
    }

    void gpio_write(Pins pin, PinValue value)
    {
        gpioWrite(get_pin_number(pin), static_cast<uint8_t>(value));
    }

    PinValue gpio_read(Pins pin)
    {
        return static_cast<PinValue>(gpioRead(get_pin_number(pin)));
    }

    void gpio_set_pwm(Pins pin, uint32_t frequency, uint32_t duty_cycle)
    {
        gpioSetPWMfrequency(get_pin_number(pin), frequency);
        gpioPWM(get_pin_number(pin), duty_cycle);
    }

    void gpio_set_event_handler(Pins pin, void (*callback)(Pins, uint32_t, uint32_t))
    {
        gpioSetAlertFuncEx(get_pin_number(pin), reinterpret_cast<gpioAlertFuncEx_t>(callback), nullptr);
    }

    void gpio_stop_pwm(Pins pin)
    {
        gpioPWM(get_pin_number(pin), 0);
    }

    void gpio_set_pull_up_down(Pins pin, PullUpDown pud)
    {
        gpioSetPullUpDown(get_pin_number(pin), static_cast<uint8_t>(pud));
    }

    void gpio_set_glitch_filter(Pins pin, uint32_t steady)
    {
        gpioGlitchFilter(get_pin_number(pin), steady);
    }

    void gpio_set_noise_filter(Pins pin, uint32_t steady, uint32_t active)
    {
        gpioNoiseFilter(get_pin_number(pin), steady, active);
    }

    void gpio_set_watchdog(Pins pin, uint32_t timeout)
    {
        gpioSetWatchdog(get_pin_number(pin), timeout);
    }

    void gpio_set_alert(Pins pin, uint32_t timeout)
    {
        gpioSetAlertFuncEx(get_pin_number(pin), nullptr, reinterpret_cast<void *>(timeout));
    }

    void gpio_set_servo_pulsewidth(Pins pin, uint32_t pulsewidth)
    {
        gpioServo(get_pin_number(pin), pulsewidth);
    }

    void gpio_set_PWM_range(Pins pin, uint32_t range)
    {
        gpioSetPWMrange(get_pin_number(pin), range);
    }

    void gpio_set_PWM_frequency(Pins pin, uint32_t frequency)
    {
        gpioSetPWMfrequency(get_pin_number(pin), frequency);
    }

    void gpio_set_PWM_dutycycle(Pins pin, uint32_t dutycycle)
    {
        gpioPWM(get_pin_number(pin), dutycycle);
    }
    void gpio_cleanup()
    {
        // Cleanup GPIO resources
        gpioTerminate();
    }
}
