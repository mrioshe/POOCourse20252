/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.methodoverloading;

/**
 *
 * @author Mauricio
 */
public class Operations {
    static int sumar(int a, int b){
    return a+b;
    }
    
    static double sumar(double c, double d){
    return c+d;
    }
    
    static double sumar(int a, int b, int e){
    return a+b+e;
    }
    
    static double sumar(int a, double c){
    return a+c;
    }
    
    static double sumar(double c, int a ){
    return a+c;
    }
}
