import matplotlib.pyplot as plt    
import numpy as np
m=1
G=6.67430e-11
M=5.972e24
orb=0
#input units: position in meters, velocity in meters per second 
#Earth's center is the origin of the coordinate system, and the x-y plane is the equatorial plane of the Earth. The z-axis is perpendicular
# to the equatorial plane. The velocity vector is in the direction of motion of the satellite.

def calculation(position_x,position_y,position_z,velocity_x,velocity_y,velocity_z):
    
    perigee_above=0

    position_vector=np.array([position_x,position_y,position_z])
    velocity_vector=np.array([velocity_x,velocity_y,velocity_z])
    orbit_energy=0.5*m*(np.linalg.norm(velocity_vector))**2-((G*m*M)/np.linalg.norm(position_vector))
    specific_angular_momentum=(np.cross(position_vector,velocity_vector))

    print("Specific Angular Momentum:", specific_angular_momentum)
    print("G*M:", G*M)

    eccentricity=np.sqrt(1+(2*orbit_energy*(np.linalg.norm(specific_angular_momentum))**2)/(m*G**2*M**2))
    #data check
    print('Eccentricity:', eccentricity)
    #data check end
    theta=np.linspace(0,2*np.pi,100)
    r=(np.linalg.norm(specific_angular_momentum)**2/((G*M))/((1+eccentricity*np.cos(theta))))
    x=(r*np.cos(theta))/1000
    y=(r*np.sin(theta))/1000
    x_earth=6371*np.cos(theta)
    y_earth=6371*np.sin(theta)

    orbital_inclination=np.dot(specific_angular_momentum,[0,0,1])/(np.linalg.norm(specific_angular_momentum))
    orb=np.arccos(orbital_inclination)
    apogee=(np.linalg.norm(specific_angular_momentum)**2/(G*M))/(1-eccentricity)
    perigee=(np.linalg.norm(specific_angular_momentum)**2/(G*M))/(1+eccentricity)
    
    cos_anomaly=(np.linalg.norm(specific_angular_momentum)**2/(G*M*np.linalg.norm(position_vector))-1)/eccentricity
    if cos_anomaly<0:
        if position_vector[2]>0:
            print('Perigee is above the equatorial plane')
            perigee_above=1
        elif position_vector[2]<0:
            print('Perigee is below the equatorial plane')
            perigee_above=0
    elif cos_anomaly>0:
        if position_vector[2]>0:
            print('Apogee is above the equatorial plane')
            perigee_above=0
        elif position_vector[2]<0:
            print('Apogee is below the equatorial plane')
            perigee_above=1
    
    #if cos_anomaly<0, the sign of the z value of the position vector shows whether the perigee is above or below the equatorial plane.
    #If the z value is positive, the perigee is above the plane, and if it is negative, the perigee is below the plane.
    #if cos_anomaly>0, the sign of the z value of the position vector shows whether the apogee is above or below the equatorial plane.
    #If the z value is positive, the apogee is above the plane, and if it is negative, the apogee is below the plane.
    #if cos_anomaly=0, I will use the velocity vector to determine the position of the perigee and apogee.
    print('Orbital Inclination:',np.abs(np.degrees(orb)))
    print('Specific Angular Momentum:', specific_angular_momentum)
    print('Apogee:', apogee/1000)
    print('Perigee:', perigee/1000)
    print('Cosine of eccentric anomaly:', cos_anomaly)
    fig, ax=plt.subplots(1,2)

    if perigee_above==1:
        x_line=np.linspace(-1*apogee/1000*np.abs(orbital_inclination),perigee/1000*np.abs(orbital_inclination),1000)
    elif perigee_above==0:
        x_line=np.linspace(-1*perigee/1000*np.abs(orbital_inclination),apogee/1000*np.abs(orbital_inclination),1000)
    y_line=np.abs(np.tan(orb))*x_line   
    print(np.linalg.norm(position_vector))


    ax[0].plot(x,y, color="red")
    ax[0].plot(x_earth,y_earth,color="blue")
    ax[1].plot(x_earth,y_earth,color="blue")
    ax[1].plot(x_line,y_line,color="red")
    ax[1].axhline(y=0, color="green", linestyle="--")
    ax[0].set_title('Orbit')
    ax[0].set_xlabel('X (km)')
    ax[0].set_ylabel('Y (km) ')
    ax[1].set_title('Inclination axis')
    ax[1].set_xlabel('X (km)')
    ax[1].set_ylabel('Y (km) ')
    ax[0].set_aspect('equal', adjustable='datalim')
    ax[1].set_aspect('equal', adjustable='datalim')
    if orbital_inclination>0:
        ax[0].text(0,0,"The satellite is following the Earth's rotation direction", fontsize=8, ha='center')
    elif orbital_inclination<0:
        ax[0].text(0,0,"The satellite is opposite to the Earth's rotation direction", fontsize=8, ha='center')
    elif orbital_inclination==0:
        ax[0].text(0,0,"The satellite is perpendicular to the equatorial plane", fontsize=8, ha='center')
    plt.grid(True)
    plt.show()





calculation(8771000,0,1000000,1000,np.sqrt(G*M/6771000),0)


