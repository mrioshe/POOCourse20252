/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.methodoverloading;

/**
 *
 * @author Mauricio
 */
public class MethodOverloading {

    public static void main(String[] args) {
        double c=3.2,d=5.0;
        int a=2,b=6,e=3;
        
        System.out.println("Sumar: " + Operations.sumar(a,b));
        System.out.println("Sumar: " + Operations.sumar(a,b,e));
        System.out.println("Sumar: " + Operations.sumar(c,d));
        
      
    }
}
