#version 330

// Input vertex attributes (from vertex shader)
in vec2 fragTexCoord;
in vec4 fragColor;

// Output fragment color
out vec4 finalColor;

// NOTE: Add here your custom variables
uniform vec4 color;

void main()
{
    // NOTE: Implement here your fragment shader code
    
    finalColor = color;
}

