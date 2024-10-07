# NXOpen Python Reference Guide:
# https://docs.plm.automation.siemens.com/data_services/resources/nx/1899/nx_api/custom/en_US/nxopen_python_ref/index.html

import NXOpen


the_session: NXOpen.Session = NXOpen.Session.GetSession()
base_part: NXOpen.BasePart = the_session.Parts.BaseWork
the_lw: NXOpen.ListingWindow = the_session.ListingWindow
work_part: NXOpen.Part = the_session.Parts.Work


def list_objects_on_layer(layer: int, list_empty_layers: bool = False) -> None:
    layer_manager: NXOpen.Layer.LayerManager = work_part.Layers
    objects_on_layer: list[NXOpen.NXObject] = layer_manager.GetAllObjectsOnLayer(layer)
    if len(objects_on_layer) == 0 and list_empty_layers == False:
        return
    the_lw.WriteFullline(f"The following {len(objects_on_layer)} items are on layer {layer}:")
    for item in objects_on_layer:
        the_lw.WriteFullline(f"\t{item.JournalIdentifier} of type {type(item)}")


def main():
    the_lw.Open()
    the_lw.WriteFullline(f"Starting Main() in {the_session.ExecutingJournal}")

    for i in range(1, 256):
        list_objects_on_layer(i)


if __name__ == '__main__':
    main()
