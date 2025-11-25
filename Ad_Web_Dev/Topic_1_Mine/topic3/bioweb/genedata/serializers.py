from rest_framework import serializers
from .models import *


class ECSerializer(serializers.ModelSerializer):
    class Meta:
        model = EC
        fields = ['id', 'ec_name']
        
class SequencingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sequencing
        fields = ['id', 'sequencing_factory', 'factory_location']

class GeneSerializer(serializers.ModelSerializer):
    ec = ECSerializer()
    sequencing = SequencingSerializer()
    class Meta:
        model = Gene
        fields = ['gene_id', 'entity', 'start', 'stop', 'sense', 'start_codon', 'ec', 'sequencing']
        
    def create(self, validated_data):
        # Extract nested data for EC and Sequencing
        ec_data = validated_data.pop('ec')
        seq_data = validated_data.pop('sequencing')

        # Resolve or create EC
        if isinstance(ec_data, dict) and ec_data.get('id') is not None:
            try:
                # Attempt to retrieve an existing EC instance by ID
                ec = EC.objects.get(pk=ec_data['id'])
            except EC.DoesNotExist:
                raise serializers.ValidationError({'ec': f"EC with id={ec_data['id']} does not exist"})
        else:
            # Create a new EC instance if no valid ID is provided
            ec = EC.objects.create(**ec_data)

        # Resolve or create Sequencing
        if isinstance(seq_data, dict) and seq_data.get('id') is not None:
            try:
                sequencing = Sequencing.objects.get(pk=seq_data['id'])
            except Sequencing.DoesNotExist:
                raise serializers.ValidationError({'sequencing': f"Sequencing with id={seq_data['id']} does not exist"})
        else:
            sequencing = Sequencing.objects.create(**seq_data)

        # Create the Gene instance  
        gene = Gene.objects.create(ec=ec, sequencing=sequencing, **validated_data)
        return gene
        
        
        
class GeneListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gene
        fields = ['id', 'gene_id']