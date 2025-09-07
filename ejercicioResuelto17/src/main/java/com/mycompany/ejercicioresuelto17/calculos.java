/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.ejercicioresuelto17;

/**
 *
 * @author Mauricio
 */
public class calculos {
    
    static double calcular_longitud_circulo(double radio) {
    double logitud_circunferencia = 2*Math.PI*radio;
    return logitud_circunferencia;
    }
    
    static double calcular_area_circulo(double radio) {
        double area_circunferencia = Math.PI*Math.pow(radio, 2);
        return area_circunferencia;
    }
}
