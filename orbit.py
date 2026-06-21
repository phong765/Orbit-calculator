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

    position_vector=np.array([position_x,position_y,position_z])
    velocity_vector=np.array([velocity_x,velocity_y,velocity_z])
    orbit_energy=0.5*m*(np.linalg.norm(velocity_vector))**2-((G*m*M)/np.linalg.norm(position_vector))
    specific_angular_momentum=(np.cross(position_vector,velocity_vector))

    eccentricity=np.sqrt(1+(2*orbit_energy*(np.linalg.norm(specific_angular_momentum))**2)/(m*G**2*M**2))
    #data check
    print('Eccentricity:', eccentricity)
    #data check end
    theta=np.linspace(0,2*np.pi,100)
    r=(np.linalg.norm(specific_angular_momentum)**2/(-G*M))/((1+eccentricity*np.cos(theta)))
    x=(r*np.cos(theta))/1000
    y=(r*np.sin(theta))/1000
    x_earth=6371*np.cos(theta)
    y_earth=6371*np.sin(theta)

    orbital_inclination=np.dot(specific_angular_momentum,[0,0,1])/(np.linalg.norm(specific_angular_momentum))
    orb=np.arccos(orbital_inclination)
    apogee=(np.linalg.norm(specific_angular_momentum)**2/(G*M))/(1-eccentricity)
    perigee=(np.linalg.norm(specific_angular_momentum)**2/(G*M))/(1+eccentricity)

    print('Orbital Inclination:',np.degrees(orb))
    print('Specific Angular Momentum:', specific_angular_momentum)
    print('Apogee:', apogee)
    print('Perigee:', perigee)
    fig, ax=plt.subplots(1,2)

    x_line=np.linspace(-10000,10000,100)
    y_line=np.tan(orb)*x_line   

    ax[0].plot(x,y)
    ax[0].plot(x_earth,y_earth)
    ax[1].plot(x_earth,y_earth)
    ax[1].plot(x_line,y_line)
    ax[0].set_title('Orbit')
    ax[0].set_xlabel('X (km)')
    ax[0].set_ylabel('Y (km) ')
    ax[1].set_title('Inclination axis')
    ax[1].set_xlabel('X (km)')
    ax[1].set_ylabel('Y (km) ')
    ax[0].set_aspect('equal', adjustable='datalim')
    ax[1].set_aspect('equal', adjustable='datalim')
    plt.grid(True)
    plt.show()
calculation(6521500,0,0,0,8000,0)

