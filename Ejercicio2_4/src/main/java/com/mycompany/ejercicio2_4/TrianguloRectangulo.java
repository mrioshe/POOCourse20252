/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.ejercicio2_4;

/**
 *
 * @author Mauricio
 */
public class TrianguloRectangulo {
    
    int base;
    int altura;
    
    TrianguloRectangulo (int base, int altura){
        this.base=base;
        this.altura=altura;
    }
    
    double calcularArea() {
        return base*altura/2;
    }
    
    double calcularHipotenusa(){
        return Math.pow(base*base+altura*altura,0.5);
    }

    double calcularPerimetro() {
        return (base+altura+calcularHipotenusa());
    }
    
    void determinarTipoTriangulo() {
        
        if ((base == altura) && (base == calcularHipotenusa()) && (altura== calcularHipotenusa())){
            System.out.println("Es un triángulo equilátero");
        } else if ((base != altura) && (base != calcularHipotenusa()) && (altura != calcularHipotenusa())){
            System.out.println("Es un triángulo escaleno");
        } else{
            System.out.println("Es un triángulo isósceles");
        }
     
    }
}
