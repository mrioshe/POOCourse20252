/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.ejercicioresuelto4;

/**
 *
 * @author Mauricio
 */
public class Calculos {
    
    static double calcular_edalber(double EDJUAN){
    double EDALBER = 2*(EDJUAN/3);
    return EDALBER;
    }
    
    static double calcular_edana(double EDJUAN) {
        double EDANA = 4 * (EDJUAN / 3);
        return EDANA;
    }
    
    static double calcular_edmama(double EDJUAN,double EDALBER,double EDANA) {
        double EDMAMA = EDJUAN+EDALBER+EDANA;
        return EDMAMA;
    }
}
