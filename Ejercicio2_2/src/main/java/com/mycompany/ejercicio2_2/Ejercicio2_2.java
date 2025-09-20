/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.ejercicio2_2;

/**
 *
 * @author Mauricio
 */
public class Ejercicio2_2 {

    public static void main(String[] args) {
        Planeta p1 =new Planeta ("Tierra",1,5.9736E24,1.0832E12,12742,150000000,tipoPlaneta.TERRESTRE, true);
        p1.imprimir();
        System.out.println("Densidad del planeta = " + p1.calcularDensidad());
        System.out.println("Es planeta exterior = " + p1.esPlanetaExtrior());
        System.out.println();
        
        Planeta p2 =new Planeta ("Jupiter",79,1.899E27,1.4313E15,13820,750000000,tipoPlaneta.GASEOSO, true);
        p1.imprimir();
        System.out.println("Densidad del planeta 2 = " + p2.calcularDensidad());
        System.out.println("Es planeta exterior 2 = " + p2.esPlanetaExtrior());
    }
}
