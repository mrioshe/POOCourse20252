/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.ejercicio2_3;

/**
 *
 * @author Mauricio
 */
public class Ejercicio2_3 {

    public static void main(String[] args) {
        Automovil auto1= new Automovil("Ford",2018,3,tipoCom.DIESEL, tipoA.EJECUTIVO,5,6,250,tipoColor.NEGRO);
        
        auto1.imprimir();
        auto1.setVelocidadActual(100);
        System.out.println("velocidad actual = " + auto1.velocidadActual);
        auto1.acelerar(20);
        System.out.println("velocidad actual = " + auto1.velocidadActual);
        auto1.desacelerar(50);
        System.out.println("velocidad actual = " + auto1.velocidadActual);
        auto1.frenar();
        System.out.println("velocidad actual = " + auto1.velocidadActual);
        auto1.desacelerar(20);
        
        
    }
}
