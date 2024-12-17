#ifndef RASPI_GPIO_H
#define RASPI_GPIO_H

#include <stdint.h>

enum PinMode
{
    INPUT = 0,
    OUTPUT = 1,
    ALT0 = 4,
    ALT1 = 5,
    ALT2 = 6,
    ALT3 = 7,
    ALT4 = 3,
    ALT5 = 2
};

enum PinValue
{
    LOW = 0,
    HIGH = 1
};

enum PullUpDown
{
    PUD_OFF = 0,
    PUD_DOWN = 1,
    PUD_UP = 2
};

enum Pins
{
    PIN_1,
    PIN_2,
    PIN_3,
    PIN_4,
    PIN_5,
    PIN_6,
    PIN_7,
    PIN_8,
    PIN_9,
    PIN_10,
    PIN_11,
    PIN_12,
    PIN_13,
    PIN_14,
    PIN_15,
    PIN_16,
    PIN_17,
    PIN_18,
    PIN_19,
    PIN_20,
    PIN_21,
    PIN_22,
    PIN_23,
    PIN_24,
    PIN_25,
    PIN_26,
    PIN_27,
    PIN_28,
    PIN_29,
    PIN_30,
    PIN_31,
    PIN_32,
    PIN_33,
    PIN_34,
    PIN_35,
    PIN_36,
    PIN_37,
    PIN_38,
    PIN_39,
    PIN_40,
};

namespace splashkit_lib
{
    void gpio_init();
    void gpio_set_mode(Pins pin, PinMode mode);
    void gpio_write(Pins pin, PinValue value);
    PinValue gpio_read(Pins pin);
    void gpio_set_pwm(Pins pin, uint32_t frequency, uint32_t duty_cycle);
    void gpio_set_event_handler(Pins pin, void (*callback)(Pins, uint32_t, uint32_t));
    void gpio_stop_pwm(Pins pin);
    void gpio_set_pull_up_down(Pins pin, PullUpDown pud);
    void gpio_set_glitch_filter(Pins pin, uint32_t steady);
    void gpio_set_noise_filter(Pins pin, uint32_t steady, uint32_t active);
    void gpio_set_watchdog(Pins pin, uint32_t timeout);
    void gpio_set_alert(Pins pin, uint32_t timeout);
    void gpio_set_servo_pulsewidth(Pins pin, uint32_t pulsewidth);
    void gpio_set_PWM_range(Pins pin, uint32_t range);
    void gpio_set_PWM_frequency(Pins pin, uint32_t frequency);
    void gpio_set_PWM_dutycycle(Pins pin, uint32_t dutycycle);
    void gpio_cleanup();
}
#endif // RASPI_GPIO_H
