/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.ejercicio8_3;

/**
 *
 * @author Mauricio
 */
public class Piramide extends FiguraGeometrica {
    private double base;
    private double altura;
    private double apotema;
    
    public Piramide(double base,double altura,double apotema){
        this.base=base;
        this.altura=altura;
        this.apotema=apotema;
        this.setVolumen(calcularVolumen());
        this.setSuperficie(calcularSuperficie());
    }
    
    public double calcularVolumen(){
        double volumen=(Math.pow(base,2.0)*altura)/3;
        return volumen;
    }
    
    public double calcularSuperficie(){
        double areaBase=Math.pow(base,2.0);
        double areaLado=2*base*apotema;
        return areaBase+areaLado;
    }
}
