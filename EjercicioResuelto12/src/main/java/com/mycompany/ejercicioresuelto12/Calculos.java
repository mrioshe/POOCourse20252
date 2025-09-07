/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.ejercicioresuelto12;

/**
 *
 * @author Mauricio
 */
public class Calculos {
    
    static double calcular_salario_bruto(double horas_laboradas, double valor_hora){
    double salario_bruto = horas_laboradas*valor_hora;
    return salario_bruto;
    }
    
    static double calcular_porcentaje_retencion(double retencion){
    double porcentaje_retención=retencion/100;
    return porcentaje_retención;
    }
    
    static double calcular_retencion_fuente(double porcentaje_retencion, double salario_bruto){
    double valor_retencion_fuente = porcentaje_retencion*salario_bruto;
    return valor_retencion_fuente;
    }
    
    
    static double calcular_salario_neto(double salario_bruto, double valor_retencion_fuente){
    double salario_neto = salario_bruto-valor_retencion_fuente;
    return salario_neto;
    }
    

    
}
