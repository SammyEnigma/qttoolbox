#include "ColorMap.h"

/// red entries for the color table. They range from 0-255
int redTable[] = 
{
	0, 84, 45,  0,  0,  0,  0,  0,
		0, 73,157,246,255,255,255,255
};

/// blue entries for the color table. They range from 0-255
int blueTable[] = 
{
	0,155,232,255,255,255,220,135,
		55,  0,  0,  0,  0,  0,  0,255
};

/// green entries for the color table. They range from 0-255
int greenTable[] = 
{
	0,  0,  0, 30,114,199,255,255,
		255,255,255,255,224,136, 53,255
};

/**********************************************************/
ColorMap::ColorMap(double minRange, 
				   double maxRange):
_minRange(minRange),
_maxRange(maxRange),
_range(maxRange-minRange)
{
	int s = sizeof(redTable)/sizeof(int);
	for (int i = 0; i < s; i++) {
		_red.push_back(redTable[i]);
		_green.push_back(greenTable[i]);
		_blue.push_back(blueTable[i]);
	}

	_tableSize = _red.size();
}

/**********************************************************/
ColorMap::~ColorMap()
{
}

/**********************************************************/
int 
ColorMap::size()
{
	return _red.size();
}

/**********************************************************/
std::vector<int>&
ColorMap::red()
{
	return _red;
}

/**********************************************************/
std::vector<int>&
ColorMap::green()
{
	return _green;
}

/**********************************************************/
std::vector<int>&
ColorMap::blue()
{
	return _blue;
}

/**********************************************************/
void
ColorMap::dataColor(double data, 
					int& red,
					int& green,
					int& blue) const
{


	int index = (int)(_tableSize* (data - _minRange)/(_range));

	if (index < 0) 
		index = 0;
	else
		if (index > _tableSize-1)
			index = _tableSize - 1;

	red = _red[index];
	blue = _blue[index];
	green = _green[index];
}

/**********************************************************/
void
ColorMap::dataColor(
		    double data, 
		    double& red,
		    double& green,
		    double& blue) const
{

	int index = (int)(_tableSize* (data - _minRange)/_range);

	if (index < 0) 
		index = 0;
	else
		if (index > _tableSize-1)
			index = _tableSize - 1;

	red = _red[index];
	blue = _blue[index];
	green = _green[index];
}

/**********************************************************/
double
ColorMap::rangeMin() 
{
	return _minRange;
}

/**********************************************************/
double
ColorMap::rangeMax() 
{
	return _maxRange;
}