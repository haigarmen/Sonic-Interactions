/* gpio - Pi gpio pins via /sys/etc */
/* see http://elinux.org/RPi_Low-level_peripherals */

/* Copyright Miller Puckette - BSD license */

#include "m_pd.h"
#include <wiringPi.h>
#include <mcp3004.h>
#include <stdio.h>

static t_class *ohEye_class;

typedef struct _ohEye {
    t_object x_obj;
    t_outlet *x_out1;
    int setup;
} t_ohEye;

static void ohEye_bang(t_ohEye *x) {
    int value, i;
    t_atom readings[16];
    for (i=0; i<8; i++) {
		value = analogRead(i+100);
		SETFLOAT(&readings[i], value);
                value = analogRead(i+108);
                SETFLOAT(&readings[i+8],value);
    }
    
    outlet_list(x->x_out1, 0, 16, readings);
//    outlet_float(x->x_out1, value);
}

static void *ohEye_new(void)
{
    t_ohEye *x = (t_ohEye *)pd_new(ohEye_class);
    x->x_out1 = outlet_new(&x->x_obj, gensym("list"));
    post("Using SPI port 0 and 1 and reading 16 ADCs");
    return (x);
}

void ohEye_setup_wiringPi(t_ohEye *x)
{
    if (x->setup==0) {
        wiringPiSetup();
        x->setup=1;
        mcp3004Setup(100, 0);
        mcp3004Setup(108, 1);
        post("OhEye is ready to read!");
    } else {
        post("OhEye is already set up!");
    }
}


void ohEye_setup(void)
{
    ohEye_class = class_new(gensym("ohEye"), 
		(t_newmethod)ohEye_new, 
		0, sizeof(t_ohEye), 
		0, A_DEFFLOAT, A_DEFFLOAT, 0);
    class_addbang(ohEye_class, ohEye_bang);
    class_addmethod(ohEye_class, (t_method)ohEye_setup_wiringPi, gensym("setup_wiringPi"), 0);
    post("OhEye Analog Inputs for Raspberry Pi version 1.0");
}
