/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.ejercicio2_4;

/**
 *
 * @author Mauricio
 */
public class Cuadrado {
    
    int lado;
    
    Cuadrado (int lado){
        this.lado=lado;
    }
    
    double calcularArea() {
        return 4*lado;
    }

    double calcularPerimetro() {
        return Math.pow(lado,2);
    }
    
}
