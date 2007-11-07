#ifndef TWOTwoKnobsSPLUGIN_H_
#define TWOTwoKnobsSPLUGIN_H_
#include <QtPlugin>
#include <QDesignerCustomWidgetInterface>

///
/// Qt plugin class for TwoKnobs.
///
class TwoKnobsPlugin: public QObject, public QDesignerCustomWidgetInterface {
	Q_OBJECT
    Q_INTERFACES(QDesignerCustomWidgetInterface)

public:
  TwoKnobsPlugin(QObject *parent = 0);
 bool isContainer() const;
     bool isInitialized() const;
     QIcon icon() const;
     QString domXml() const;
     QString group() const;
     QString includeFile() const;
     QString name() const;
     QString toolTip() const;
     QString whatsThis() const;
     QWidget *createWidget(QWidget *parent);
     void initialize(QDesignerFormEditorInterface *core);

private:
	bool initialized;

};

#endif
